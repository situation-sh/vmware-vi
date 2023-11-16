# HAErrorsAtDest

The destination compute resource is HA-enabled, and HA is not running properly.  This will cause the following problems: 1\\) The VM will not have HA protection. 2\\) If this is an intracluster VMotion, HA will not be properly informed that the migration completed. This can have serious consequences to the functioning of HA.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ha_errors_at_dest import HAErrorsAtDest

# TODO update the JSON string below
json = "{}"
# create an instance of HAErrorsAtDest from a JSON string
ha_errors_at_dest_instance = HAErrorsAtDest.from_json(json)
# print the JSON string representation of the object
print HAErrorsAtDest.to_json()

# convert the object into a dict
ha_errors_at_dest_dict = ha_errors_at_dest_instance.to_dict()
# create an instance of HAErrorsAtDest from a dict
ha_errors_at_dest_form_dict = ha_errors_at_dest.from_dict(ha_errors_at_dest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


