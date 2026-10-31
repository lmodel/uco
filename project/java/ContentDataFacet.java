package example;

/* metamodel_version: 1.12.0 */
/* version: 1.5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A content data facet is a grouping of characteristics unique to a block of digital data.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ContentDataFacet extends Facet {

  private String byteOrder;
  private String dataPayload;
  private ObservableObject dataPayloadReferenceURL;
  private BigDecimal entropy;
  private List<Hash> hash;
  private Boolean isEncrypted;
  private String magicNumber;
  private String mimeClass;
  private List<String> mimeType;
  private Integer sizeInBytes;


}