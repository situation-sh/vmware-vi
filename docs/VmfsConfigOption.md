# VmfsConfigOption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_size_option** | **int** | Supported values of VMFS block size in kilobytes (KB) *HostVmfsVolume.blockSize*.  ***Since:*** vSphere API 6.5  | 
**unmap_granularity_option** | **List[int]** | Supported values of VMFS unmap granularity *HostVmfsVolume.unmapGranularity*.  The unit is KB.  ***Since:*** vSphere API 6.5  | [optional] 
**unmap_bandwidth_fixed_value** | [**LongOption**](LongOption.md) |  | [optional] 
**unmap_bandwidth_dynamic_min** | [**LongOption**](LongOption.md) |  | [optional] 
**unmap_bandwidth_dynamic_max** | [**LongOption**](LongOption.md) |  | [optional] 
**unmap_bandwidth_increment** | **int** | Increment value of unmap bandwidth  ***Since:*** vSphere API 6.7  | [optional] 
**unmap_bandwidth_ultra_low** | **int** | Fixed unmap bandwidth ultra low limit value in MB/sec.  | [optional] 

## Example

```python
from vmware_vi.models.vmfs_config_option import VmfsConfigOption

# TODO update the JSON string below
json = "{}"
# create an instance of VmfsConfigOption from a JSON string
vmfs_config_option_instance = VmfsConfigOption.from_json(json)
# print the JSON string representation of the object
print VmfsConfigOption.to_json()

# convert the object into a dict
vmfs_config_option_dict = vmfs_config_option_instance.to_dict()
# create an instance of VmfsConfigOption from a dict
vmfs_config_option_form_dict = vmfs_config_option.from_dict(vmfs_config_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


