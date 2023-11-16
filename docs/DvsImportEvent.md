# DvsImportEvent

This event is generated when a import operation is performed on a distributed virtual switch  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_type** | **str** | The type of restore operation.  See *EntityImportType_enum* for valid values  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.dvs_import_event import DvsImportEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsImportEvent from a JSON string
dvs_import_event_instance = DvsImportEvent.from_json(json)
# print the JSON string representation of the object
print DvsImportEvent.to_json()

# convert the object into a dict
dvs_import_event_dict = dvs_import_event_instance.to_dict()
# create an instance of DvsImportEvent from a dict
dvs_import_event_form_dict = dvs_import_event.from_dict(dvs_import_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


