# CompositePolicyOption

DataObject represents a composite Policy that is created by the user using different PolicyOptions.  The options set in the CompositePolicyOption should be derived from the possible options as indicated by the CompositePolicyOptionMetadata.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option** | [**List[PolicyOption]**](PolicyOption.md) | List of policy options that are composed and applicable for this composite policy option.  The selected PolicyOptions in a CompositePolicyOption will be used in the policy. PolicyOptions need not be specified if they are not desired for the CompositePolicyOption. Order of PolicyOptions in the PolicyOption array is not significant. The host profile policy engine will not respect order of PolicyOptions. It will apply PolicyOptions in a pre-determined order. Clients of the API must produce PolicyOption in the same order as specified in the metadata.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.composite_policy_option import CompositePolicyOption

# TODO update the JSON string below
json = "{}"
# create an instance of CompositePolicyOption from a JSON string
composite_policy_option_instance = CompositePolicyOption.from_json(json)
# print the JSON string representation of the object
print CompositePolicyOption.to_json()

# convert the object into a dict
composite_policy_option_dict = composite_policy_option_instance.to_dict()
# create an instance of CompositePolicyOption from a dict
composite_policy_option_form_dict = composite_policy_option.from_dict(composite_policy_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


