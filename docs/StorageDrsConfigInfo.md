# StorageDrsConfigInfo

The *StorageDrsConfigInfo* data object describes storage DRS configuration for a pod *StoragePod*.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod_config** | [**StorageDrsPodConfigInfo**](StorageDrsPodConfigInfo.md) |  | 
**vm_config** | [**List[StorageDrsVmConfigInfo]**](StorageDrsVmConfigInfo.md) | List of virtual machine configurations for the storage DRS service.  Each entry applies to all the virtual disks of the virtual machine on this pod.  If a virtual machine is not specified in this array, the service uses the default settings for that virtual machine.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.storage_drs_config_info import StorageDrsConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsConfigInfo from a JSON string
storage_drs_config_info_instance = StorageDrsConfigInfo.from_json(json)
# print the JSON string representation of the object
print StorageDrsConfigInfo.to_json()

# convert the object into a dict
storage_drs_config_info_dict = storage_drs_config_info_instance.to_dict()
# create an instance of StorageDrsConfigInfo from a dict
storage_drs_config_info_form_dict = storage_drs_config_info.from_dict(storage_drs_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


