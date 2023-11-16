# CustomizationSysprepRebootOptionEnum

A enum constant specifying what should be done to the guest vm after running sysprep.  Possible values: - `reboot`: Reboot the machine after running sysprep.      This will cause values   specified in the sysprep.xml to be applied immediately. - `noreboot`: Take no action.      Leave the guest os running after running sysprep. This   option can be used to look at values for debugging purposes after   running sysprep. - `shutdown`: Shutdown the machine after running sysprep.      This puts the vm in a   sealed state.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


