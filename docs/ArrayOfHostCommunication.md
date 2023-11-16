# ArrayOfHostCommunication

A boxed array of *HostCommunication*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostCommunication]**](HostCommunication.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_communication import ArrayOfHostCommunication

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostCommunication from a JSON string
array_of_host_communication_instance = ArrayOfHostCommunication.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostCommunication.to_json()

# convert the object into a dict
array_of_host_communication_dict = array_of_host_communication_instance.to_dict()
# create an instance of ArrayOfHostCommunication from a dict
array_of_host_communication_form_dict = array_of_host_communication.from_dict(array_of_host_communication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


