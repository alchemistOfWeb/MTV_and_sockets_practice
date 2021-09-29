import sys, settings, core, seeds, migrations


def get_functions_from_module(module_obj):
    return [obj for (name, obj) in vars(module_obj).items() 
            if hasattr(obj, '__class__') and obj.__class__.__name__ == 'function']


if __name__ == '__main__':
    if len(sys.argv) > 0:
        command = sys.argv[1]        

        if command == 'runserver':
            # core.DB.get_connection()            
            server = core.Server.get_instance()
            server.run()
            
        elif command == 'migrate':
            migrate_functions = get_functions_from_module(migrations)
        elif command == 'seed':
            seed_functions = get_functions_from_module(seeds)
