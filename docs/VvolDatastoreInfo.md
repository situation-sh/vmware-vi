# VvolDatastoreInfo

Detailed information about a VirtualVolume datastore.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vvol_ds** | [**HostVvolVolume**](HostVvolVolume.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vvol_datastore_info import VvolDatastoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VvolDatastoreInfo from a JSON string
vvol_datastore_info_instance = VvolDatastoreInfo.from_json(json)
# print the JSON string representation of the object
print VvolDatastoreInfo.to_json()

# convert the object into a dict
vvol_datastore_info_dict = vvol_datastore_info_instance.to_dict()
# create an instance of VvolDatastoreInfo from a dict
vvol_datastore_info_form_dict = vvol_datastore_info.from_dict(vvol_datastore_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


