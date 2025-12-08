from app.init import create_app


from src.managers.start_manager import StartManager
from src.managers.store_manager import StoreManager
from src.managers.recipe_manager import RecipeManager


from src.utils.logging.logger import Logger
from src.utils.logging.log_writer import LogWriter


from src.settings_manager import SettingManager


def _init_managers():
    settings_manager = SettingManager()
    settings = settings_manager.settings
    LogWriter(settings_manager).setup()

    StartManager().init(settings)
    StoreManager().init()
    RecipeManager().init()



app = create_app()


if __name__ == '__main__':
    _init_managers()
    Logger.info('main', 'Application starting')
    app.run(debug = True, port = 8080)