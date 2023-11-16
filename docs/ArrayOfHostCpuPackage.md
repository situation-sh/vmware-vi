# ArrayOfHostCpuPackage

A boxed array of *HostCpuPackage*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostCpuPackage]**](HostCpuPackage.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_cpu_package import ArrayOfHostCpuPackage

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostCpuPackage from a JSON string
array_of_host_cpu_package_instance = ArrayOfHostCpuPackage.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostCpuPackage.to_json()

# convert the object into a dict
array_of_host_cpu_package_dict = array_of_host_cpu_package_instance.to_dict()
# create an instance of ArrayOfHostCpuPackage from a dict
array_of_host_cpu_package_form_dict = array_of_host_cpu_package.from_dict(array_of_host_cpu_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


