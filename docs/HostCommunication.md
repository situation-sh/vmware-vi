# HostCommunication

A HostCommunication fault is thrown if an error happened while communicating to a host.  This would typically be due to network connections or server failures. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_communication import HostCommunication

# TODO update the JSON string below
json = "{}"
# create an instance of HostCommunication from a JSON string
host_communication_instance = HostCommunication.from_json(json)
# print the JSON string representation of the object
print HostCommunication.to_json()

# convert the object into a dict
host_communication_dict = host_communication_instance.to_dict()
# create an instance of HostCommunication from a dict
host_communication_form_dict = host_communication.from_dict(host_communication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


