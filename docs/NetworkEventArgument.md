# NetworkEventArgument

The event argument is a Network object.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.network_event_argument import NetworkEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkEventArgument from a JSON string
network_event_argument_instance = NetworkEventArgument.from_json(json)
# print the JSON string representation of the object
print NetworkEventArgument.to_json()

# convert the object into a dict
network_event_argument_dict = network_event_argument_instance.to_dict()
# create an instance of NetworkEventArgument from a dict
network_event_argument_form_dict = network_event_argument.from_dict(network_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


