# DatacenterEventArgument

The event argument is a Datacenter object. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.datacenter_event_argument import DatacenterEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of DatacenterEventArgument from a JSON string
datacenter_event_argument_instance = DatacenterEventArgument.from_json(json)
# print the JSON string representation of the object
print DatacenterEventArgument.to_json()

# convert the object into a dict
datacenter_event_argument_dict = datacenter_event_argument_instance.to_dict()
# create an instance of DatacenterEventArgument from a dict
datacenter_event_argument_form_dict = datacenter_event_argument.from_dict(datacenter_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


