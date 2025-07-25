import re

from infrahub_sdk.checks import InfrahubCheck

RE_TAG = re.compile(r"^color-[a-z]+")


class ColorTagsCheck(InfrahubCheck):
    query = "tags_query"  # This references the query name in .infrahub.yml

    def validate(self, data):
        for tag in data["BuiltinTag"]["edges"]:
            if not RE_TAG.match(tag["node"]["name"]["value"]):
                self.log_error(
                    message=f"Invalid tag name: {tag['node']['name']['value']}. Tag names must follow pattern 'color-[name]'",
                    object_id=tag["node"]["name"]["value"],
                    object_type="BuiltinTag",
                )
