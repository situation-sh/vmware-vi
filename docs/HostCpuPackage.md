# HostCpuPackage

Information about a physical CPU package. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Package index, starting from zero.  | 
**vendor** | **str** | CPU vendor name, possible names currently are \&quot;Intel\&quot;, \&quot;AMD\&quot;, \&quot;arm\&quot;, \&quot;hygon\&quot;, or \&quot;unknown\&quot;.  | 
**hz** | **int** | CPU speed in HZ.  | 
**bus_hz** | **int** | Bus speed in HZ.  | 
**description** | **str** | String summary description of CPU (for display purposes).  | 
**thread_id** | **List[int]** | The logical CPU threads on this package.  | 
**cpu_feature** | [**List[HostCpuIdInfo]**](HostCpuIdInfo.md) | The CPU feature bit on this particular CPU.  This is independent of the product and licensing capabilities.  | [optional] 

## Example

```python
from vmware_vi.models.host_cpu_package import HostCpuPackage

# TODO update the JSON string below
json = "{}"
# create an instance of HostCpuPackage from a JSON string
host_cpu_package_instance = HostCpuPackage.from_json(json)
# print the JSON string representation of the object
print HostCpuPackage.to_json()

# convert the object into a dict
host_cpu_package_dict = host_cpu_package_instance.to_dict()
# create an instance of HostCpuPackage from a dict
host_cpu_package_form_dict = host_cpu_package.from_dict(host_cpu_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


