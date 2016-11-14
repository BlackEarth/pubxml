<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.1" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	 xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
	 xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas"
	 xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
	 xmlns:o="urn:schemas-microsoft-com:office:office"
	 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
	 xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math"
	 xmlns:v="urn:schemas-microsoft-com:vml"
	 xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing"
	 xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
	 xmlns:w10="urn:schemas-microsoft-com:office:word"
	 xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml"
	 xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml"
	 xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup"
	 xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk"
	 xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml"
	 xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape"
	 exclude-result-prefixes="w wpc mc o r m v wp14 wp w10 w14 w15 wpg wpi wne wps">

    <xsl:output method="xml" encoding="utf-8"/>

	<xsl:template match="@*|node()"><xsl:copy><xsl:apply-templates select="@*|node()"/></xsl:copy></xsl:template>

	<!-- clobber any remaining Word tags -->
	<xsl:template match="w:*"><xsl:apply-templates/></xsl:template>
	<xsl:template match="wpc:*"><xsl:apply-templates/></xsl:template>
	<xsl:template match="mc:*"><xsl:apply-templates/></xsl:template>
	<xsl:template match="o:*"><xsl:apply-templates/></xsl:template>
	<xsl:template match="r:*"><xsl:apply-templates/></xsl:template>
	<xsl:template match="m:*"><xsl:apply-templates/></xsl:template>
	<xsl:template match="v:*"><xsl:apply-templates/></xsl:template>
	<xsl:template match="wp14:*"><xsl:apply-templates/></xsl:template>
	<xsl:template match="wp:*"><xsl:apply-templates/></xsl:template>
	<xsl:template match="w10:*"><xsl:apply-templates/></xsl:template>
	<xsl:template match="w14:*"><xsl:apply-templates/></xsl:template>
	<xsl:template match="w15:*"><xsl:apply-templates/></xsl:template>
	<xsl:template match="wpg:*"><xsl:apply-templates/></xsl:template>
	<xsl:template match="wpi:*"><xsl:apply-templates/></xsl:template>
	<xsl:template match="wne:*"><xsl:apply-templates/></xsl:template>
	<xsl:template match="wps:*"><xsl:apply-templates/></xsl:template>

</xsl:stylesheet>