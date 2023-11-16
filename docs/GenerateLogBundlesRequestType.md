# GenerateLogBundlesRequestType

The parameters of *DiagnosticManager.GenerateLogBundles_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_default** | **bool** | Specifies if the bundle should include the default server. If called on a VirtualCenter server, then this means the VirtualCenter diagnostic files. If called directly on a host, then includeDefault must be set to true.  | 
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Lists hosts that are included. This is only used when called on VirtualCenter. If called directly on a host, then this parameter must be empty.  Refers instances of *HostSystem*.  | [optional] 

## Example

```python
from vmware_vi.models.generate_log_bundles_request_type import GenerateLogBundlesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateLogBundlesRequestType from a JSON string
generate_log_bundles_request_type_instance = GenerateLogBundlesRequestType.from_json(json)
# print the JSON string representation of the object
print GenerateLogBundlesRequestType.to_json()

# convert the object into a dict
generate_log_bundles_request_type_dict = generate_log_bundles_request_type_instance.to_dict()
# create an instance of GenerateLogBundlesRequestType from a dict
generate_log_bundles_request_type_form_dict = generate_log_bundles_request_type.from_dict(generate_log_bundles_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


