# NasVolumeNotMounted

This fault is thrown when an operation to configure a NAS datastore fails because the specified NFS volume is not mounted.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_host** | **str** | The host that runs the NFS server.  ***Since:*** vSphere API 4.0  | 
**remote_path** | **str** | The remote share.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.nas_volume_not_mounted import NasVolumeNotMounted

# TODO update the JSON string below
json = "{}"
# create an instance of NasVolumeNotMounted from a JSON string
nas_volume_not_mounted_instance = NasVolumeNotMounted.from_json(json)
# print the JSON string representation of the object
print NasVolumeNotMounted.to_json()

# convert the object into a dict
nas_volume_not_mounted_dict = nas_volume_not_mounted_instance.to_dict()
# create an instance of NasVolumeNotMounted from a dict
nas_volume_not_mounted_form_dict = nas_volume_not_mounted.from_dict(nas_volume_not_mounted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


