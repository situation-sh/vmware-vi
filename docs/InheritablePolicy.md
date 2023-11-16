# InheritablePolicy

The base class for any type of setting or configuration that may get a inherited value.  When used in a reconfigure operation specification, if *InheritablePolicy.inherited* is true, it specifies the intention to change the values of subclass's properties to the inherited values from the level above. In this case, users don't need to specify the values and any set property in the subclass will be ignored. if *InheritablePolicy.inherited* is false, it specifies the intention to explicitly set subclass's properties to user specified values. Users should set the properties in the subclass with the desired values.  When used in a configuration information object, The values of the properties in the subclass are the effective values. if *InheritablePolicy.inherited* is true, the object is getting the effective values from upper level. If false, the values are explicitly set by a user.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inherited** | **bool** | Whether the configuration is set to inherited value.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.inheritable_policy import InheritablePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of InheritablePolicy from a JSON string
inheritable_policy_instance = InheritablePolicy.from_json(json)
# print the JSON string representation of the object
print InheritablePolicy.to_json()

# convert the object into a dict
inheritable_policy_dict = inheritable_policy_instance.to_dict()
# create an instance of InheritablePolicy from a dict
inheritable_policy_form_dict = inheritable_policy.from_dict(inheritable_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


