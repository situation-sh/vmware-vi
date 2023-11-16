# DvsFilterPolicy

This class defines Network Filter Policy.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_config** | [**List[DvsFilterConfig]**](DvsFilterConfig.md) | List of Network Filter Configurations.  In an update operation, the array can contain all *DvsTrafficFilterConfigSpec* objects or all *DvsFilterConfig* and *DvsTrafficFilterConfig* object, but not mixed of Config and Spec objects. If array of *DvsFilterConfigSpec* and *DvsTrafficFilterConfigSpec* is used for updating Network Filter then only the Network Filters matching *DistributedVirtualPort.key* / *DistributedVirtualPort.key* is updated. If array of *DvsFilterConfig* and *DvsTrafficFilterConfig* is used for updating port settings, the Network Filter settings will be overridden with the new array specified. The specified array should only contain *DvsFilterConfig* and *DvsTrafficFilterConfig* objects with *InheritablePolicy.inherited* / *InheritablePolicy.inherited* set to false. *DvsFilterConfig*/*DvsTrafficFilterConfig* objects with *InheritablePolicy.inherited*/*InheritablePolicy.inherited* as true in the specified array will be ignored. The updated result will include *DvsFilterConfig*/*DvsTrafficFilterConfig* objects inherited from parent, if any.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.dvs_filter_policy import DvsFilterPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DvsFilterPolicy from a JSON string
dvs_filter_policy_instance = DvsFilterPolicy.from_json(json)
# print the JSON string representation of the object
print DvsFilterPolicy.to_json()

# convert the object into a dict
dvs_filter_policy_dict = dvs_filter_policy_instance.to_dict()
# create an instance of DvsFilterPolicy from a dict
dvs_filter_policy_form_dict = dvs_filter_policy.from_dict(dvs_filter_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


