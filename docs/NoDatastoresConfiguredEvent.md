# NoDatastoresConfiguredEvent

No datastores have been configured on the host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.no_datastores_configured_event import NoDatastoresConfiguredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of NoDatastoresConfiguredEvent from a JSON string
no_datastores_configured_event_instance = NoDatastoresConfiguredEvent.from_json(json)
# print the JSON string representation of the object
print NoDatastoresConfiguredEvent.to_json()

# convert the object into a dict
no_datastores_configured_event_dict = no_datastores_configured_event_instance.to_dict()
# create an instance of NoDatastoresConfiguredEvent from a dict
no_datastores_configured_event_form_dict = no_datastores_configured_event.from_dict(no_datastores_configured_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


