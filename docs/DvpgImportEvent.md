# DvpgImportEvent

This event is generated when an import operation is performed on a distributed virtual portgroup  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_type** | **str** | The type of restore operation.  See *EntityImportType_enum* for valid values  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.dvpg_import_event import DvpgImportEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvpgImportEvent from a JSON string
dvpg_import_event_instance = DvpgImportEvent.from_json(json)
# print the JSON string representation of the object
print DvpgImportEvent.to_json()

# convert the object into a dict
dvpg_import_event_dict = dvpg_import_event_instance.to_dict()
# create an instance of DvpgImportEvent from a dict
dvpg_import_event_form_dict = dvpg_import_event.from_dict(dvpg_import_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


