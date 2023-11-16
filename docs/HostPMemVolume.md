# HostPMemVolume

The VMFS file system.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | The universally unique identifier assigned to PMem volume.  ***Since:*** vSphere API 6.7  | 
**version** | **str** | Version of the PMem FS  ***Since:*** vSphere API 6.7  | 

## Example

```python
from vmware_vi.models.host_p_mem_volume import HostPMemVolume

# TODO update the JSON string below
json = "{}"
# create an instance of HostPMemVolume from a JSON string
host_p_mem_volume_instance = HostPMemVolume.from_json(json)
# print the JSON string representation of the object
print HostPMemVolume.to_json()

# convert the object into a dict
host_p_mem_volume_dict = host_p_mem_volume_instance.to_dict()
# create an instance of HostPMemVolume from a dict
host_p_mem_volume_form_dict = host_p_mem_volume.from_dict(host_p_mem_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


