from infrahub_sdk.generator import InfrahubGenerator


class WidgetGenerator(InfrahubGenerator):
    async def generate(self, data: dict) -> None:
        # Access the widget as an SDK object
        widget = self.nodes[
            0
        ]  # or self.store.get(data["TestWidget"]["edges"][0]["node"]["id"])
        widget_name: str = widget.name.value
        widget_count: int = widget.count.value

        # Create resources based on widget count
        for count in range(1, widget_count + 1):
            payload = {
                "name": f"{widget_name.lower()}-{count}",
            }
            obj = await self.client.create(kind="TestResource", data=payload)
            await obj.save(allow_upsert=True)
            await obj.save(allow_upsert=True)
            await obj.save(allow_upsert=True)
