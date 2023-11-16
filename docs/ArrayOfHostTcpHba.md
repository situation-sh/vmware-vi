# ArrayOfHostTcpHba

A boxed array of *HostTcpHba*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostTcpHba]**](HostTcpHba.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_tcp_hba import ArrayOfHostTcpHba

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostTcpHba from a JSON string
array_of_host_tcp_hba_instance = ArrayOfHostTcpHba.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostTcpHba.to_json()

# convert the object into a dict
array_of_host_tcp_hba_dict = array_of_host_tcp_hba_instance.to_dict()
# create an instance of ArrayOfHostTcpHba from a dict
array_of_host_tcp_hba_form_dict = array_of_host_tcp_hba.from_dict(array_of_host_tcp_hba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


