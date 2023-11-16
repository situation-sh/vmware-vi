# HostVvolVolumeSpecification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_size_in_mb** | **int** | Maximum size of the container  ***Since:*** vSphere API 6.0  | 
**volume_name** | **str** | Container name.  ***Since:*** vSphere API 6.0  | 
**vasa_provider_info** | [**List[VimVasaProviderInfo]**](VimVasaProviderInfo.md) | VASA Providers that manage this volume  ***Since:*** vSphere API 6.0  | [optional] 
**storage_array** | [**List[VASAStorageArray]**](VASAStorageArray.md) | Storage Array  ***Since:*** vSphere API 6.0  | [optional] 
**uuid** | **str** | Vendor specified storage-container ID  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.host_vvol_volume_specification import HostVvolVolumeSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of HostVvolVolumeSpecification from a JSON string
host_vvol_volume_specification_instance = HostVvolVolumeSpecification.from_json(json)
# print the JSON string representation of the object
print HostVvolVolumeSpecification.to_json()

# convert the object into a dict
host_vvol_volume_specification_dict = host_vvol_volume_specification_instance.to_dict()
# create an instance of HostVvolVolumeSpecification from a dict
host_vvol_volume_specification_form_dict = host_vvol_volume_specification.from_dict(host_vvol_volume_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


