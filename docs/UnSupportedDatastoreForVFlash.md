# UnSupportedDatastoreForVFlash

VFlash is not supported on the datastore.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore_name** | **str** | The name of the Datastore.  ***Since:*** vSphere API 5.5  | 
**type** | **str** | Datastore file system volume type.  See *DatastoreSummary.type*  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.un_supported_datastore_for_v_flash import UnSupportedDatastoreForVFlash

# TODO update the JSON string below
json = "{}"
# create an instance of UnSupportedDatastoreForVFlash from a JSON string
un_supported_datastore_for_v_flash_instance = UnSupportedDatastoreForVFlash.from_json(json)
# print the JSON string representation of the object
print UnSupportedDatastoreForVFlash.to_json()

# convert the object into a dict
un_supported_datastore_for_v_flash_dict = un_supported_datastore_for_v_flash_instance.to_dict()
# create an instance of UnSupportedDatastoreForVFlash from a dict
un_supported_datastore_for_v_flash_form_dict = un_supported_datastore_for_v_flash.from_dict(un_supported_datastore_for_v_flash_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


