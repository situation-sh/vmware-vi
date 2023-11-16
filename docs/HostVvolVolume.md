# HostVvolVolume


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sc_id** | **str** | The universally unique identifier assigned to vvolDS.  ***Since:*** vSphere API 6.0  | 
**host_pe** | [**List[VVolHostPE]**](VVolHostPE.md) |  | [optional] 
**vasa_provider_info** | [**List[VimVasaProviderInfo]**](VimVasaProviderInfo.md) | VASA Providers that manage this volume  ***Since:*** vSphere API 6.0  | [optional] 
**storage_array** | [**List[VASAStorageArray]**](VASAStorageArray.md) | List of storage array serving this VVol based storage container  ***Since:*** vSphere API 6.0  | [optional] 
**protocol_endpoint_type** | **str** | Backing protocol of the datastore  | [optional] 

## Example

```python
from vmware_vi.models.host_vvol_volume import HostVvolVolume

# TODO update the JSON string below
json = "{}"
# create an instance of HostVvolVolume from a JSON string
host_vvol_volume_instance = HostVvolVolume.from_json(json)
# print the JSON string representation of the object
print HostVvolVolume.to_json()

# convert the object into a dict
host_vvol_volume_dict = host_vvol_volume_instance.to_dict()
# create an instance of HostVvolVolume from a dict
host_vvol_volume_form_dict = host_vvol_volume.from_dict(host_vvol_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


