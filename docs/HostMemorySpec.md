# HostMemorySpec

DataObject used for configuring the memory setting  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_console_reservation** | **int** | Service Console reservation in bytes.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_memory_spec import HostMemorySpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostMemorySpec from a JSON string
host_memory_spec_instance = HostMemorySpec.from_json(json)
# print the JSON string representation of the object
print HostMemorySpec.to_json()

# convert the object into a dict
host_memory_spec_dict = host_memory_spec_instance.to_dict()
# create an instance of HostMemorySpec from a dict
host_memory_spec_form_dict = host_memory_spec.from_dict(host_memory_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


