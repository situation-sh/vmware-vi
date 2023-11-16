# CryptoSpecNoOp

This data object type indicates that the encryption settings of the virtual machine or disk should not be modified by the operation.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.crypto_spec_no_op import CryptoSpecNoOp

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoSpecNoOp from a JSON string
crypto_spec_no_op_instance = CryptoSpecNoOp.from_json(json)
# print the JSON string representation of the object
print CryptoSpecNoOp.to_json()

# convert the object into a dict
crypto_spec_no_op_dict = crypto_spec_no_op_instance.to_dict()
# create an instance of CryptoSpecNoOp from a dict
crypto_spec_no_op_form_dict = crypto_spec_no_op.from_dict(crypto_spec_no_op_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


