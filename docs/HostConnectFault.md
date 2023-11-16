# HostConnectFault

A base clase for faults that are related to connecting or adding a host to the inventory. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_connect_fault import HostConnectFault

# TODO update the JSON string below
json = "{}"
# create an instance of HostConnectFault from a JSON string
host_connect_fault_instance = HostConnectFault.from_json(json)
# print the JSON string representation of the object
print HostConnectFault.to_json()

# convert the object into a dict
host_connect_fault_dict = host_connect_fault_instance.to_dict()
# create an instance of HostConnectFault from a dict
host_connect_fault_form_dict = host_connect_fault.from_dict(host_connect_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


