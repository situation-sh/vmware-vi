# DvsTrafficRuleset

This class defines a ruleset(set of rules) that will be applied to network traffic.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the ruleset.  ***Since:*** vSphere API 5.5  | [optional] 
**enabled** | **bool** | Whether ruleset is enabled or not.  ***Since:*** vSphere API 5.5  | [optional] 
**precedence** | **int** | Precedence of the ruleset.  Rulesets for a port will be executed in the order of their precedence.  ***Since:*** vSphere API 5.5  | [optional] 
**rules** | [**List[DvsTrafficRule]**](DvsTrafficRule.md) | List of rules belonging to this ruleset.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.dvs_traffic_ruleset import DvsTrafficRuleset

# TODO update the JSON string below
json = "{}"
# create an instance of DvsTrafficRuleset from a JSON string
dvs_traffic_ruleset_instance = DvsTrafficRuleset.from_json(json)
# print the JSON string representation of the object
print DvsTrafficRuleset.to_json()

# convert the object into a dict
dvs_traffic_ruleset_dict = dvs_traffic_ruleset_instance.to_dict()
# create an instance of DvsTrafficRuleset from a dict
dvs_traffic_ruleset_form_dict = dvs_traffic_ruleset.from_dict(dvs_traffic_ruleset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


