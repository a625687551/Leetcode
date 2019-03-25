#include <iostream>
#include <vector>

using namespace std;

class CMyString
{
  public:
    CMyString(char *pData = nullptr);
    CMyString(const CMyString &str);
    ~CMyString(void);

    void Print();

  private:
    char *m_pData;
};
