# StorageDrsHmsMoveInProgress

This fault is thrown HMS service is in the process of moving a subset of disks for which Storage DRS recommendation is generated.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.storage_drs_hms_move_in_progress import StorageDrsHmsMoveInProgress

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsHmsMoveInProgress from a JSON string
storage_drs_hms_move_in_progress_instance = StorageDrsHmsMoveInProgress.from_json(json)
# print the JSON string representation of the object
print StorageDrsHmsMoveInProgress.to_json()

# convert the object into a dict
storage_drs_hms_move_in_progress_dict = storage_drs_hms_move_in_progress_instance.to_dict()
# create an instance of StorageDrsHmsMoveInProgress from a dict
storage_drs_hms_move_in_progress_form_dict = storage_drs_hms_move_in_progress.from_dict(storage_drs_hms_move_in_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


