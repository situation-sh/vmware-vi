# PodDiskLocator

The disk locator class.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_id** | **int** | The disk ID.  ***Since:*** vSphere API 5.0  | 
**disk_move_type** | **str** | The disk move type.  ***Since:*** vSphere API 5.0  | [optional] 
**disk_backing_info** | [**VirtualDeviceBackingInfo**](VirtualDeviceBackingInfo.md) |  | [optional] 
**profile** | [**List[VirtualMachineProfileSpec]**](VirtualMachineProfileSpec.md) | Virtual Disk Profile requirement.  Profiles are solution specific. Profile Based Storage Management is a vSphere server extension. The API users who want to provision VMs using Storage Profiles, need to interact with it. This is an optional parameter and if user doesn&#39;t specify profile, the default behavior will apply.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.pod_disk_locator import PodDiskLocator

# TODO update the JSON string below
json = "{}"
# create an instance of PodDiskLocator from a JSON string
pod_disk_locator_instance = PodDiskLocator.from_json(json)
# print the JSON string representation of the object
print PodDiskLocator.to_json()

# convert the object into a dict
pod_disk_locator_dict = pod_disk_locator_instance.to_dict()
# create an instance of PodDiskLocator from a dict
pod_disk_locator_form_dict = pod_disk_locator.from_dict(pod_disk_locator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


