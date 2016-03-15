import argparse
import sys
import os
import json


parser = argparse.ArgumentParser(description=('Zatt. An implementation of'
                                              'the Raft algorithm for '
                                              'distributed consensus'))
parser.add_argument('-c', '--config', dest='path_config',
                    help='Config file path. Default: zatt.conf')
parser.add_argument('-i', '--id', help='This node ID. Default: 0', default=0)
parser.add_argument('-a', '--address', help=('This node address. Default: '
                    '127.0.0.1'))
parser.add_argument('-p', '--port', help='This node port. Default: 5254')
parser.add_argument('-s', '--storage', help=('Path for the persistent state'
                    ' file. Default: zatt.persist'), dest='path_storage')
parser.add_argument('--node-id', action='append', default=[],
                    help='Remote node id')
parser.add_argument('--node-address', action='append', default=[],
                    help='Remote node address')
parser.add_argument('--node-port', action='append', default=[],
                    help='Remote node port')

def config():
    args = parser.parse_args()
    if len(args.node_id) != len(args.node_port)\
    or len(args.node_id) != len(args.node_address):
        print('There should be the same number of:node-id, node-address,',
              'node-port')
        sys.exit(1)
    if args.path_config is not None and not os.path.isfile(args.path_config):
        print('Config file not found')
        sys.exit(1)

    config = {'id':args.id, 'cluster': {}}

    path = args.path_config if args.path_config else 'zatt.conf'
    if os.path.isfile(path):
        with open(path, 'r') as f:
            config.update(json.loads(f.read()))

    if 'storage' not in config:
        config['storage'] = 'zatt.persist'

    if args.path_storage:
        config['storage'] = args.path_storage

    for x in zip(args.node_id, args.node_address, args.node_port):
        config['cluster'][x[0]] = x[1:3]

    if config['id'] not in config['cluster']:
        config['cluster'][config['id']] = ['127.0.0.1', '5254']

    if args.address:
        config['cluster'][config['id']][0] = args.address

    if args.port:
        config['cluster'][config['id']][1] = args.port

    cluster = config['cluster']
    config['cluster'] = {}
    for k,v in cluster.items():
        config['cluster'][int(k)] = {'info': tuple(v)}

    return config
