# ArrayOfNoDatastoresConfiguredEvent

A boxed array of *NoDatastoresConfiguredEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NoDatastoresConfiguredEvent]**](NoDatastoresConfiguredEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_no_datastores_configured_event import ArrayOfNoDatastoresConfiguredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNoDatastoresConfiguredEvent from a JSON string
array_of_no_datastores_configured_event_instance = ArrayOfNoDatastoresConfiguredEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfNoDatastoresConfiguredEvent.to_json()

# convert the object into a dict
array_of_no_datastores_configured_event_dict = array_of_no_datastores_configured_event_instance.to_dict()
# create an instance of ArrayOfNoDatastoresConfiguredEvent from a dict
array_of_no_datastores_configured_event_form_dict = array_of_no_datastores_configured_event.from_dict(array_of_no_datastores_configured_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


