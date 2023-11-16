# BaseConfigInfoFileBackingInfo

Information for file backing of a virtual storage object.  File backing is mainly used for virtual disks.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_path** | **str** | Full file path for the host file used in this backing.  ***Since:*** vSphere API 6.5  | 
**backing_object_id** | **str** | Id refers to the backed storage object where the virtual storage object is backed on.  ***Since:*** vSphere API 6.5  | [optional] 
**parent** | [**BaseConfigInfoFileBackingInfo**](BaseConfigInfoFileBackingInfo.md) |  | [optional] 
**delta_size_in_mb** | **int** | Size allocated by the FS for this file/chain/link/extent only.  This property is used only for a delta disk whose *BaseConfigInfoFileBackingInfo.parent* is set.  ***Since:*** vSphere API 6.5  | [optional] 
**key_id** | [**CryptoKeyId**](CryptoKeyId.md) |  | [optional] 

## Example

```python
from vmware_vi.models.base_config_info_file_backing_info import BaseConfigInfoFileBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BaseConfigInfoFileBackingInfo from a JSON string
base_config_info_file_backing_info_instance = BaseConfigInfoFileBackingInfo.from_json(json)
# print the JSON string representation of the object
print BaseConfigInfoFileBackingInfo.to_json()

# convert the object into a dict
base_config_info_file_backing_info_dict = base_config_info_file_backing_info_instance.to_dict()
# create an instance of BaseConfigInfoFileBackingInfo from a dict
base_config_info_file_backing_info_form_dict = base_config_info_file_backing_info.from_dict(base_config_info_file_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


