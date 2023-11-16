# StorageDrsHmsUnreachable

This fault is thrown when Storage DRS cannot connect to HMS service or HMS APIs invoked by Storage DRS error out due to connection issues.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.storage_drs_hms_unreachable import StorageDrsHmsUnreachable

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsHmsUnreachable from a JSON string
storage_drs_hms_unreachable_instance = StorageDrsHmsUnreachable.from_json(json)
# print the JSON string representation of the object
print StorageDrsHmsUnreachable.to_json()

# convert the object into a dict
storage_drs_hms_unreachable_dict = storage_drs_hms_unreachable_instance.to_dict()
# create an instance of StorageDrsHmsUnreachable from a dict
storage_drs_hms_unreachable_form_dict = storage_drs_hms_unreachable.from_dict(storage_drs_hms_unreachable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


