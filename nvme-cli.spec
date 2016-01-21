%global commit0 bdbb4da0979fbdc079cf98410cdb31cf799e83b3
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           nvme-cli
Version:        0.2
Release:        2.20160112git%{shortcommit0}%{?dist}
Summary:        NVMe management command line interface

License:        GPLv2+
URL:            https://github.com/linux-nvme/nvme-cli
Source0:        https://github.com/linux-nvme/%{name}/archive/%{commit0}.tar.gz

BuildRequires:  systemd-devel

%description
nvme-cli provides NVM-Express user space tooling for Linux.

%prep
%setup -qn %{name}-%{commit0}


%build
make PREFIX=/usr CFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}" %{?_smp_mflags}


%install
%make_install PREFIX=/usr


%files
%license LICENSE
%doc README.md
%{_sbindir}/nvme
%{_mandir}/man1/nvme*.gz


%changelog
* Wed Jan 20 2016 luto@kernel.org - 0.2-2.20160112gitbdbb4da
- Update to new upstream commit, fixing #49.  "nvme list" now works.

* Wed Jan 13 2016 luto@kernel.org - 0.2-1.20160112gitde3e0f1
- Initial import.
