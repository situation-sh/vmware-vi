# ArrayOfHostTargetTransport

A boxed array of *HostTargetTransport*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostTargetTransport]**](HostTargetTransport.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_target_transport import ArrayOfHostTargetTransport

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostTargetTransport from a JSON string
array_of_host_target_transport_instance = ArrayOfHostTargetTransport.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostTargetTransport.to_json()

# convert the object into a dict
array_of_host_target_transport_dict = array_of_host_target_transport_instance.to_dict()
# create an instance of ArrayOfHostTargetTransport from a dict
array_of_host_target_transport_form_dict = array_of_host_target_transport.from_dict(array_of_host_target_transport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


