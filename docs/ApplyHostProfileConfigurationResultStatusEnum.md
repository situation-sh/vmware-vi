# ApplyHostProfileConfigurationResultStatusEnum

Possible values: - `success`: Remediation succeeded. - `failed`: Remediation failed. - `reboot_failed`: Remediation succeeded but reboot after remediation failed.      May treat this as a warning. - `stateless_reboot_failed`: Stateless reboot for remediation failed. - `check_compliance_failed`: Remediation and reboot succeeded but check compliance after reboot   failed.      May treat this as a warning. - `state_not_satisfied`: The required state is not satisfied so host profiel apply cannot   be done. - `exit_maintenancemode_failed`: Exit maintenance mode failed. - `canceled`: The remediation was canceled.    ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


