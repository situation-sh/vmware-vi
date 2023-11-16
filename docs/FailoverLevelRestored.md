# FailoverLevelRestored

This event records that the amount of cluster resources has increased and is now sufficient to satisfy the configured HA failover level. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.failover_level_restored import FailoverLevelRestored

# TODO update the JSON string below
json = "{}"
# create an instance of FailoverLevelRestored from a JSON string
failover_level_restored_instance = FailoverLevelRestored.from_json(json)
# print the JSON string representation of the object
print FailoverLevelRestored.to_json()

# convert the object into a dict
failover_level_restored_dict = failover_level_restored_instance.to_dict()
# create an instance of FailoverLevelRestored from a dict
failover_level_restored_form_dict = failover_level_restored.from_dict(failover_level_restored_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


