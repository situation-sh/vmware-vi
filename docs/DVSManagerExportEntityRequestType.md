# DVSManagerExportEntityRequestType

The parameters of *DistributedVirtualSwitchManager.DVSManagerExportEntity_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selection_set** | [**List[SelectionSet]**](SelectionSet.md) | The selection criteria for a set of entities to export the configuration.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.dvs_manager_export_entity_request_type import DVSManagerExportEntityRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DVSManagerExportEntityRequestType from a JSON string
dvs_manager_export_entity_request_type_instance = DVSManagerExportEntityRequestType.from_json(json)
# print the JSON string representation of the object
print DVSManagerExportEntityRequestType.to_json()

# convert the object into a dict
dvs_manager_export_entity_request_type_dict = dvs_manager_export_entity_request_type_instance.to_dict()
# create an instance of DVSManagerExportEntityRequestType from a dict
dvs_manager_export_entity_request_type_form_dict = dvs_manager_export_entity_request_type.from_dict(dvs_manager_export_entity_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


