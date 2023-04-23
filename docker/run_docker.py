# yinying edit this file from deepmind alphafold repo

"""Docker launch script for PPRCODE docker image."""

import os
import pathlib
import signal
from typing import Tuple

from absl import app
from absl import flags
from absl import logging
import docker
from docker import types

flags.DEFINE_string(
    'fasta', None, 'input FASTA file(s) for scan.')
flags.DEFINE_enum(
    'program', 'ps_scan', ['ps_scan', 'pprfinder'],
    'Choose a proper algorithm to process your sequence. PPRCODE use PS_Scan(ps_scan) by default. However, you may use PPRfinder(pprfinder) from Small\'s Lab')
flags.DEFINE_string(
    'bin_dir', '/app/bin/', 'Where additional required binaries locate.')
flags.DEFINE_string(
    'profile_dir', '/app/profiles/', 'Where additional required profiles locate.')
flags.DEFINE_bool(
    'report', True, 'Generate a human-friendly report file in xlsx format')
flags.DEFINE_string(
    'save_dir', './results', 'Path to save run results.')
flags.DEFINE_enum(
    'plot_color_scheme', 'RdBu',
    ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap',
     'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r',
     'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r',
     'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples',
     'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r',
     'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia',
     'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot',
     'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r',
     'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix',
     'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat',
     'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r',
     'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r',
     'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r',
     'ocean'],
    'Color scheme for plot')
flags.DEFINE_list(
    'plot_item', ['bar', 'ppr', 'rna', 'type', 'edge'], 'plot PPRCODE results in what ways.')

flags.DEFINE_string(
    'docker_image_name', 'pprcode', 'Name of the PPRCODE Docker image.')

flags.DEFINE_bool(
    'run_benchmark', False, 'Fetch a benchmark dataset. **This could make your job running messy.**')

flags.DEFINE_bool(
    'debug', False, 'debug messages')

flags.DEFINE_bool(
    'fix_gap', False, 'Fix gap in sequence scanning results. Turn it off so that the results will not be weird.')

flags.DEFINE_string(
    'docker_user', f'{os.geteuid()}:{os.getegid()}',
    'UID:GID with which to run the Docker container. The output directories '
    'will be owned by this user:group. By default, this is the current user. '
    'Valid options are: uid or uid:gid, non-numeric values are not recognised '
    'by Docker unless that user has been created within the container.')

FLAGS = flags.FLAGS
try:
    _ROOT_MOUNT_DIRECTORY = f'/home/{os.getlogin()}'
except:
    _ROOT_MOUNT_DIRECTORY = pathlib.Path('.').resolve()
    os.makedirs(_ROOT_MOUNT_DIRECTORY, exist_ok=True)

def _create_mount(mount_name: str, path: str) -> Tuple[types.Mount, str]:
    """Create a mount point for each file and directory used by the model."""
    path = pathlib.Path(path).absolute()
    target_path = pathlib.Path(_ROOT_MOUNT_DIRECTORY, mount_name)

    if path.is_dir():
        source_path = path
        mounted_path = target_path
    else:
        source_path = path.parent
        mounted_path = pathlib.Path(target_path, path.name)
    if not source_path.exists():
        raise ValueError(f'Failed to find source directory "{source_path}" to '
                         'mount in Docker container.')
    print('Mounting %s -> %s', source_path, target_path)
    mount = types.Mount(target=str(target_path), source=str(source_path),
                        type='bind', read_only=True)
    return mount, str(mounted_path)


def main(argv):
    if len(argv) > 1:
        raise app.UsageError('Too many command-line arguments.')

    mounts = []
    command_args = []

    fasta = pathlib.Path(FLAGS.fasta).resolve()
    save_dir = pathlib.Path(FLAGS.save_dir).resolve()


    os.makedirs(save_dir, exist_ok=True)


    mount, target_path = _create_mount('input', str(fasta))
    mounts.append(mount)
    command_args.append(f'--fasta={target_path}')

    output_target_path = os.path.join(_ROOT_MOUNT_DIRECTORY, 'output')
    mounts.append(types.Mount(output_target_path, str(save_dir), type='bind'))
    command_args.append(f'--save_dir={output_target_path}')

    if FLAGS.debug: command_args.append(f'--debug')
    if FLAGS.report: command_args.append(f'--report')
    if FLAGS.run_benchmark: command_args.append(f'--run_benchmark')
    if FLAGS.fix_gap: command_args.append(f'--fix_gap')

    command_args.extend([
        f'--program={FLAGS.program}',
        f'--bin_dir={FLAGS.bin_dir}',
        f'--profile_dir={FLAGS.profile_dir}',
        f'--plot_color_scheme={FLAGS.plot_color_scheme}',
        f'--plot_item={",".join(FLAGS.plot_item)}',

    ])

    # for item in FLAGS.plot_item:
    #     command_args.append(f'--plot_item={item}')

    print(command_args)

    client = docker.from_env()

    container = client.containers.run(
        image=FLAGS.docker_image_name,
        command=command_args,
        remove=True,
        detach=True,
        mounts=mounts,
        user=FLAGS.docker_user,
    )

    # Add signal handler to ensure CTRL+C also stops the running container.
    signal.signal(signal.SIGINT,
                  lambda unused_sig, unused_frame: container.kill())

    for line in container.logs(stream=True):
        print(line.strip().decode('utf-8'))


if __name__ == '__main__':
    flags.mark_flags_as_required([
        'fasta',
    ])
    app.run(main)
