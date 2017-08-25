# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# coding:utf-8
from __future__ import unicode_literals

from django.db import models


class AnalysisMaster(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    reference_genome = models.CharField(max_length=45, blank=True, null=True)
    compare_method = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analysis_master'


class CompareTable(models.Model):
    master_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=45, blank=True, null=True)
    comparison_name = models.CharField(max_length=45, blank=True, null=True)
    sample_group1 = models.CharField(max_length=45, blank=True, null=True)
    sample_group2 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compare_table'


class DnaSampleSequencingType(models.Model):
    project_id = models.IntegerField()
    resequencing = models.CharField(max_length=1, blank=True, null=True)
    de_novo_sequencing = models.CharField(max_length=1, blank=True, null=True)
    mate_pair = models.CharField(max_length=1, blank=True, null=True)
    low_initial_weight_sequencing = models.CharField(max_length=1, blank=True, null=True)
    exome = models.CharField(max_length=1, blank=True, null=True)
    target_area_capture = models.CharField(max_length=1, blank=True, null=True)
    purified = models.CharField(max_length=1, blank=True, null=True)
    unpurified = models.CharField(max_length=1, blank=True, null=True)
    d16s_rdna = models.CharField(max_length=1, blank=True, null=True)
    rad = models.CharField(max_length=1, blank=True, null=True)
    metagenome = models.CharField(max_length=1, blank=True, null=True)
    chip_seq = models.CharField(max_length=1, blank=True, null=True)
    dna_methylation_sequencing = models.CharField(max_length=1, blank=True, null=True)
    rrbs = models.CharField(max_length=1, blank=True, null=True)
    medip_seq = models.CharField(max_length=1, blank=True, null=True)
    mitochondrial_dna_sequencing = models.CharField(max_length=1, blank=True, null=True)
    dna_sample_sequencing_type_other = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dna_sample_sequencing_type'


class RnaSampleSequencingType(models.Model):
    project_id = models.IntegerField()
    three_eukaryotic_mrna_seq = models.CharField(max_length=1, blank=True, null=True)
    mrna_seq_prokaryotae = models.CharField(max_length=1, blank=True, null=True)
    low_initial_amount_of_eukaryotic_mrna_seq = models.CharField(max_length=1, blank=True, null=True)
    strand_specific_transcriptome = models.CharField(max_length=1, blank=True, null=True)
    incrna_seq = models.CharField(max_length=1, blank=True, null=True)
    c_dna_transcriptome = models.CharField(max_length=1, blank=True, null=True)
    cdna_single_cell_transcriptom = models.CharField(max_length=1, blank=True, null=True)
    small_rna_sequencing = models.CharField(max_length=1, blank=True, null=True)
    plasma_small_rna_equencing = models.CharField(max_length=1, blank=True, null=True)
    rna_sample_sequencing_type_other = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rna_sample_sequencing_type'


class SampleInfoDetail(models.Model):
    project_id = models.IntegerField()
    project_number = models.CharField(max_length=45, unique=True)
    sample_name = models.CharField(max_length=45)
    sample_id = models.CharField(max_length=45, unique=True)
    express_number = models.CharField(max_length=45, blank=True, null=True)
    product_num = models.CharField(max_length=45, blank=True, null=True)
    sendsample_time = models.CharField(max_length=45, blank=True, null=True)
    sendsample_comment = models.CharField(max_length=100, blank=True, null=True)
    rin = models.CharField(max_length=45, blank=True, null=True)
    concentration = models.CharField(max_length=45, blank=True, null=True)
    volume = models.CharField(max_length=45, blank=True, null=True)
    qualitycheck_results = models.CharField(max_length=1, blank=True, null=True)
    qualitycheck_time = models.CharField(max_length=45, blank=True, null=True)
    qualitycheck_comment = models.CharField(max_length=100, blank=True, null=True)
    lib_id = models.CharField(max_length=45, blank=True, null=True)
    lib_time = models.CharField(max_length=45, blank=True, null=True)
    lib_comment = models.CharField(max_length=100, blank=True, null=True)
    upmachine_type = models.CharField(max_length=45, blank=True, null=True)
    upmachine_mode = models.CharField(max_length=45, blank=True, null=True)
    upmachine_num = models.CharField(max_length=45, blank=True, null=True)
    upmachine_time = models.CharField(max_length=45, blank=True, null=True)
    upmachine_comment = models.CharField(max_length=100, blank=True, null=True)
    downmachine_num = models.CharField(max_length=45, blank=True, null=True)
    q20 = models.CharField(max_length=45, blank=True, null=True)
    q30 = models.CharField(max_length=45, blank=True, null=True)
    downmachine_time = models.CharField(max_length=45, blank=True, null=True)
    downmachine_comment = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sample_info_detail'


class SampleOther(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    reagent_kit_method = models.CharField(max_length=1, blank=True, null=True)
    ctab_method = models.CharField(max_length=1, blank=True, null=True)
    trizol_method = models.CharField(max_length=1, blank=True, null=True)
    other_method = models.CharField(max_length=45, blank=True, null=True)
    berry_handel = models.CharField(max_length=1, blank=True, null=True)
    ret_handel = models.CharField(max_length=1, blank=True, null=True)
    other_handel = models.CharField(max_length=45, blank=True, null=True)
    accord_contract = models.CharField(max_length=1, blank=True, null=True)
    special_needs = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample_other'


class SamplePacketInformation(models.Model):
    master_id = models.IntegerField(blank=True, null=True)
    sample_id_alias = models.CharField(max_length=45, blank=True, null=True)
    sample_group = models.CharField(max_length=45, blank=True, null=True)
    repeated_experiment = models.CharField(max_length=45, blank=True, null=True)
    sample_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample_packet_information'


class SampleProjectMaster(models.Model):
    id = models.IntegerField(primary_key=True)
    project_number = models.CharField(max_length=45, unique=True, blank=True, null=True)
    project_name = models.TextField(blank=True, null=True)
    cust_organization = models.TextField(blank=True, null=True)
    cust_user = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    cust_tel = models.CharField(max_length=45, blank=True, null=True)
    sale_name = models.CharField(max_length=45, blank=True, null=True)
    sp_delive_date = models.CharField(max_length=45, blank=True, null=True)
    sp_sum = models.CharField(max_length=45, blank=True, null=True)
    species = models.CharField(max_length=45, blank=True, null=True)
    project_leader = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.CharField(max_length=45, blank=True, null=True)
    #project_log = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample_project_master'


class SampleSpecies(models.Model):
    project_id = models.IntegerField()
    lyophillization = models.CharField(max_length=1, blank=True, null=True)
    te_buffer = models.CharField(max_length=1, blank=True, null=True)
    ddh2o = models.CharField(max_length=1, blank=True, null=True)
    depc = models.CharField(max_length=1, blank=True, null=True)
    sample_species_other = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample_species'


class SampleTable(models.Model):
    sample_id = models.CharField(unique=True, max_length=50)
    project_id = models.IntegerField()
    sample_name = models.CharField(max_length=50, blank=True, null=True)
    sepcies = models.CharField(max_length=50, blank=True, null=True)
    product_num = models.CharField(max_length=50, blank=True, null=True)
    library_type = models.CharField(max_length=50, blank=True, null=True)
    concentration = models.CharField(max_length=50, blank=True, null=True)
    volume = models.CharField(max_length=50, blank=True, null=True)
    data_quantity = models.CharField(max_length=50, blank=True, null=True)
    fragment_length = models.CharField(max_length=50, blank=True, null=True)
    od_260_or_280 = models.CharField(max_length=50, blank=True, null=True)
    od_260_or_230 = models.CharField(max_length=50, blank=True, null=True)
    comment = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample_table'


class SampleType(models.Model):
    project_id = models.IntegerField()
    genomic_dna = models.CharField(max_length=1, blank=True, null=True)
    chip_dna = models.CharField(max_length=1, blank=True, null=True)
    pcr_fragment = models.CharField(max_length=1, blank=True, null=True)
    free_dna = models.CharField(max_length=1, blank=True, null=True)
    mitochondrial_dna = models.CharField(max_length=1, blank=True, null=True)
    others_dna = models.CharField(max_length=45, blank=True, null=True)
    total_rna = models.CharField(max_length=1, blank=True, null=True)
    to_ribosomal_rna = models.CharField(max_length=1, blank=True, null=True)
    small_rna = models.CharField(max_length=1, blank=True, null=True)
    c_dna = models.CharField(max_length=1, blank=True, null=True)
    plasma_rna = models.CharField(max_length=1, blank=True, null=True)
    other_rna = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample_type'


class UserInfo(models.Model):
    username = models.CharField(unique=True, max_length=45)
    customer_name = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45)
    e_mail = models.CharField(max_length=45, blank=True, null=True)
    tel = models.CharField(max_length=45, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=2, blank=True, null=True)
    role = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    field = models.CharField(max_length=100, blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True, null=True)

    def get_password(self):
        return self.password

    class Meta:
        managed = False
        db_table = 'user_info'


class Attachment(models.Model):
    # id = models.AutoField(primary_key=True)
    # id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    upload_user_id = models.IntegerField()
    operate_user_id = models.IntegerField()
    file_type = models.CharField(max_length=45, blank=True, null=True)
    filename = models.CharField(max_length=200, blank=True, null=True)
    file_path = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    upload_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attachment'


class SendSample(models.Model):
    project_id = models.IntegerField()
    project_number = models.CharField(max_length=45, unique=True)
    sample_name = models.CharField(max_length=45)
    species = models.CharField(max_length=45)
    om_id = models.CharField(max_length=100)
    express_number = models.CharField(max_length=45, blank=True, null=True)
    product_num = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
    upload_time = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'send_sample'


class QualityCheck(models.Model):
    project_id = models.IntegerField()
    project_number = models.CharField(max_length=45, unique=True)
    sample_name = models.CharField(max_length=45)
    om_id = models.CharField(max_length=100)
    sample_id = models.CharField(max_length=45, unique=True)
    concentration = models.CharField(max_length=45, blank=True, null=True)
    volume = models.CharField(max_length=45, blank=True, null=True)
    rin = models.CharField(max_length=45, blank=True, null=True)
    results = models.CharField(max_length=1, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
    upload_time = models.CharField(max_length=45, blank=True, null=True)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quality_check'


class BuildLib(models.Model):
    project_id = models.IntegerField()
    project_number = models.CharField(max_length=45, unique=True)
    sample_name = models.CharField(max_length=45)
    om_id = models.CharField(max_length=100)
    sample_id = models.CharField(max_length=45, unique=True)
    lib_id = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
    upload_time = models.CharField(max_length=45, blank=True, null=True)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'build_lib'


class UpMachine(models.Model):
    project_id = models.IntegerField()
    project_number = models.CharField(max_length=45, unique=True)
    sample_name = models.CharField(max_length=45)
    om_id = models.CharField(max_length=100)
    sample_id = models.CharField(max_length=45, unique=True)
    upmachinetype = models.CharField(max_length=45, blank=True, null=True)
    mode = models.CharField(max_length=45, blank=True, null=True)
    data_count = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
    upload_time = models.CharField(max_length=45, blank=True, null=True)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upmachine'


class DownMachine(models.Model):
    project_id = models.IntegerField()
    project_number = models.CharField(max_length=45, unique=True)
    sample_name = models.CharField(max_length=45)
    om_id = models.CharField(max_length=100)
    sample_id = models.CharField(max_length=45, unique=True)
    data_count = models.CharField(max_length=45, blank=True, null=True)
    q20 = models.CharField(max_length=45, blank=True, null=True)
    q30 = models.CharField(max_length=45, blank=True, null=True)
    data_count = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
    upload_time = models.CharField(max_length=45, blank=True, null=True)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'downmachine'


class BillingInfo(models.Model):
    project_id = models.IntegerField()
    project_number = models.CharField(max_length=45, blank=True, null=True)
    expense = models.IntegerField(blank=True, null=True)
    billing_number = models.CharField(max_length=45, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billing_info'


class ReceiptInfo(models.Model):
    project_id = models.IntegerField()
    project_number = models.CharField(max_length=45, blank=True, null=True)
    expense = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'receipt_info'


class CostInfo(models.Model):
    project_id = models.IntegerField()
    project_number = models.CharField(max_length=45, blank=True, null=True)
    expense = models.IntegerField(blank=True, null=True)
    sample_number = models.CharField(max_length=45, blank=True, null=True)
    unit_cost = models.CharField(max_length=45, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost_info'


class LogInfo(models.Model):
    project_id = models.IntegerField()
    action = models.CharField(max_length=45, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    manager = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_log_table'


class ReturnSample(models.Model):
    sample_name = models.CharField(max_length=45)
    sample_id = models.CharField(max_length=45)
    location = models.CharField(max_length=100)
    time = models.DateTimeField(blank=True, null=True)
    upload_time = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_sample'

