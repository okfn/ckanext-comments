import ckan.plugins as plugins
import ckan.plugins.toolkit as tk
from ckan.lib.plugins import DefaultTranslation

import ckanext.comments.helpers as helpers
import ckanext.comments.logic.action as action
import ckanext.comments.logic.auth as auth
import ckanext.comments.logic.validators as validators

try:
    config_declarations = tk.blanket.config_declarations
except AttributeError:
    config_declarations = lambda cls: cls


@config_declarations
class CommentsPlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IAuthFunctions)
    plugins.implements(plugins.IActions)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IValidators)
    plugins.implements(plugins.ITranslation)

    # IConfigurer

    def update_config(self, config_):
        tk.add_template_directory(config_, "templates")
        tk.add_public_directory(config_, "public")
        tk.add_resource("assets", "comments")

    # IAuthFunctions

    def get_auth_functions(self):
        return auth.get_auth_functions()

    # IActions

    def get_actions(self):
        return action.get_actions()

    # ITemplateHelpers

    def get_helpers(self):
        return helpers.get_helpers()

    # IValidators

    def get_validators(self):
        return validators.get_validators()

    # ITranslation

    def i18n_locales(self):
        """Lanaguages this plugin has translations for."""
        # Return a list of languages that this plugin has translations for.
        return ["es", "en"]

    def i18n_domain(self):
        """The domain for this plugin's translations."""
        # Return the translation domain for this plugin.
        return "ckanext-comments"
