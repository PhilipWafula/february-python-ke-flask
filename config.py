import configparser, os

API_VERSION = '0.0.1'

# get absolute path for config file
CONFIG_FILE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))

# get environment on which API is running
DEPLOYMENT_ENVIRONMENT = os.environ.get('DEPLOYMENT_NAME') or 'development'

# ensure console shows dev environment they are running on:
print('CURRENT DEPLOYMENT ENVIRONMENT: ' + DEPLOYMENT_ENVIRONMENT)

# get config file name
CONFIG_FILENAME = '{}_config.ini'.format(DEPLOYMENT_ENVIRONMENT.lower())

# define config parsers
common_config_file_parser = configparser.ConfigParser()
specific_config_file_parser = configparser.ConfigParser()

# get folder for path for config files
common_config_file_folder_path = os.path.join(CONFIG_FILE_DIRECTORY, 'configs/common_config.ini')
specific_config_file_folder_path = os.path.join(CONFIG_FILE_DIRECTORY, 'configs/' + CONFIG_FILENAME)

if not os.path.isfile(common_config_file_folder_path):
    raise Exception("Missing Common Config File")

if not os.path.isfile(specific_config_file_folder_path):
    raise Exception("Missing Config File: {}".format(CONFIG_FILENAME))

common_config_file_parser.read(common_config_file_folder_path)
specific_config_file_parser.read(specific_config_file_folder_path)

# get deployment
DEPLOYMENT_NAME = specific_config_file_parser['APP']['DEPLOYMENT_NAME']

# check that the deployment name specified by the env matches the one in the config file
if DEPLOYMENT_ENVIRONMENT.lower() != DEPLOYMENT_NAME.lower():
    raise RuntimeError('deployment name in env ({}) does not match that in config ({}), aborting'.format(
        DEPLOYMENT_ENVIRONMENT.lower(),
        DEPLOYMENT_NAME.lower()))

# define checks for deployment environment
IS_TEST = specific_config_file_parser['APP'].getboolean('IS_TEST', False)
IS_PRODUCTION = specific_config_file_parser['APP'].getboolean('IS_PRODUCTION')

DATABASE_USER = os.environ.get("DATABASE_USER") or specific_config_file_parser['DATABASE'].get('user') \
                or '{}_{}'.format(common_config_file_parser['DATABASE']['user'], DEPLOYMENT_NAME.replace("-", "_"))

DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD") or specific_config_file_parser['DATABASE']['password']

DATABASE_HOST = specific_config_file_parser['DATABASE']['host']

DATABASE_NAME = specific_config_file_parser['DATABASE'].get('database') \
                or common_config_file_parser['DATABASE']['database']

DATABASE_PORT = specific_config_file_parser['DATABASE'].get('port') or common_config_file_parser['DATABASE']['port']


def get_database_uri(name, host, censored=True):
    return 'postgresql://{}:{}@{}:{}/{}'.format(DATABASE_USER,
                                                '*******' if censored else DATABASE_PASSWORD,
                                                host,
                                                DATABASE_PORT,
                                                name)


SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE_NAME, DATABASE_HOST, censored=False)
CENSORED_URI = get_database_uri(DATABASE_NAME, DATABASE_HOST, censored=True)

print('Working database URI: ' + CENSORED_URI)
SQLALCHEMY_TRACK_MODIFICATIONS = False

