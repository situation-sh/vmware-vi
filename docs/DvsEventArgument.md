# DvsEventArgument

The event argument is a Host object.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dvs** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.dvs_event_argument import DvsEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of DvsEventArgument from a JSON string
dvs_event_argument_instance = DvsEventArgument.from_json(json)
# print the JSON string representation of the object
print DvsEventArgument.to_json()

# convert the object into a dict
dvs_event_argument_dict = dvs_event_argument_instance.to_dict()
# create an instance of DvsEventArgument from a dict
dvs_event_argument_form_dict = dvs_event_argument.from_dict(dvs_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


