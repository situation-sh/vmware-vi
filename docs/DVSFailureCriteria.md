# DVSFailureCriteria

This data object type describes the network adapter failover detection algorithm for a network adapter team.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_speed** | [**StringPolicy**](StringPolicy.md) |  | [optional] 
**speed** | [**IntPolicy**](IntPolicy.md) |  | [optional] 
**check_duplex** | [**BoolPolicy**](BoolPolicy.md) |  | [optional] 
**full_duplex** | [**BoolPolicy**](BoolPolicy.md) |  | [optional] 
**check_error_percent** | [**BoolPolicy**](BoolPolicy.md) |  | [optional] 
**percentage** | [**IntPolicy**](IntPolicy.md) |  | [optional] 
**check_beacon** | [**BoolPolicy**](BoolPolicy.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dvs_failure_criteria import DVSFailureCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of DVSFailureCriteria from a JSON string
dvs_failure_criteria_instance = DVSFailureCriteria.from_json(json)
# print the JSON string representation of the object
print DVSFailureCriteria.to_json()

# convert the object into a dict
dvs_failure_criteria_dict = dvs_failure_criteria_instance.to_dict()
# create an instance of DVSFailureCriteria from a dict
dvs_failure_criteria_form_dict = dvs_failure_criteria.from_dict(dvs_failure_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


