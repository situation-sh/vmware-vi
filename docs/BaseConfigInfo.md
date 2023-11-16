# BaseConfigInfo

This data object type contains the basic configuration for a virtual storage object or a virtual storage object snapshot.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**name** | **str** | Descriptive name of this object.  ***Since:*** vSphere API 6.5  | 
**create_time** | **datetime** | The date and time this object was created.  ***Since:*** vSphere API 6.5  | 
**keep_after_delete_vm** | **bool** | Choice of the deletion behavior of this virtual storage object.  If not set, the default value is false.  ***Since:*** vSphere API 6.7  | [optional] 
**relocation_disabled** | **bool** | Is virtual storage object relocation disabled.  If not set, the default value is false.  ***Since:*** vSphere API 6.7  | [optional] 
**native_snapshot_supported** | **bool** | Is virtual storage object supports native snapshot.  If not set, the default value is false.  ***Since:*** vSphere API 6.7  | [optional] 
**changed_block_tracking_enabled** | **bool** | If Virtua storage object has changed block tracking enabled.  If not set, the default value is false.  ***Since:*** vSphere API 6.7  | [optional] 
**backing** | [**BaseConfigInfoBackingInfo**](BaseConfigInfoBackingInfo.md) |  | 
**metadata** | [**List[KeyValue]**](KeyValue.md) | Metadata associated with the FCD if available.  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**vclock** | [**VslmVClockInfo**](VslmVClockInfo.md) |  | [optional] 
**iofilter** | **List[str]** | IDs of the IO Filters associated with the virtual disk.  See *IoFilterInfo.id*. The client cannot modify this information on a virtual machine.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.base_config_info import BaseConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BaseConfigInfo from a JSON string
base_config_info_instance = BaseConfigInfo.from_json(json)
# print the JSON string representation of the object
print BaseConfigInfo.to_json()

# convert the object into a dict
base_config_info_dict = base_config_info_instance.to_dict()
# create an instance of BaseConfigInfo from a dict
base_config_info_form_dict = base_config_info.from_dict(base_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


