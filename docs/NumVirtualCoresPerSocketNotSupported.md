# NumVirtualCoresPerSocketNotSupported

The host's software does not support enough cores per socket to accommodate the virtual machine.  This is always an error.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_supported_cores_per_socket_dest** | **int** | The maximum number of cores per socket supported on the host.  ***Since:*** vSphere API 5.0  | 
**num_cores_per_socket_vm** | **int** | The number of cores per socket in the virtual machine.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.num_virtual_cores_per_socket_not_supported import NumVirtualCoresPerSocketNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of NumVirtualCoresPerSocketNotSupported from a JSON string
num_virtual_cores_per_socket_not_supported_instance = NumVirtualCoresPerSocketNotSupported.from_json(json)
# print the JSON string representation of the object
print NumVirtualCoresPerSocketNotSupported.to_json()

# convert the object into a dict
num_virtual_cores_per_socket_not_supported_dict = num_virtual_cores_per_socket_not_supported_instance.to_dict()
# create an instance of NumVirtualCoresPerSocketNotSupported from a dict
num_virtual_cores_per_socket_not_supported_form_dict = num_virtual_cores_per_socket_not_supported.from_dict(num_virtual_cores_per_socket_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


